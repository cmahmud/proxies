# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 404
- HTTP: 137 alive / 81 gold
- HTTPS: 61 alive / 28 gold
- SOCKS4: 164 alive / 142 gold
- SOCKS5: 183 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48040
- Ever gold: 1515

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
