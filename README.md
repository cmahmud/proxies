# SyndProxy validated proxy pool

## Current pool

- Alive now: 445
- Gold now: 358
- HTTP: 76 alive / 46 gold
- HTTPS: 30 alive / 10 gold
- SOCKS4: 163 alive / 153 gold
- SOCKS5: 176 alive / 149 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48309
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
