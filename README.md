# SyndProxy private pool

## Current pool

- Alive now: 940
- Gold now: 362
- HTTP: 321 alive / 86 gold
- HTTPS: 186 alive / 24 gold
- SOCKS4: 226 alive / 144 gold
- SOCKS5: 207 alive / 108 gold

## Historical pool

- Discovered: 165832
- Ever alive: 32353
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
