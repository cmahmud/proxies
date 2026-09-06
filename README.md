# SyndProxy validated proxy pool

## Current pool

- Alive now: 442
- Gold now: 362
- HTTP: 71 alive / 54 gold
- HTTPS: 31 alive / 13 gold
- SOCKS4: 167 alive / 151 gold
- SOCKS5: 173 alive / 144 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48256
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
