# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 400
- HTTP: 87 alive / 65 gold
- HTTPS: 39 alive / 17 gold
- SOCKS4: 178 alive / 155 gold
- SOCKS5: 183 alive / 163 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48145
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
