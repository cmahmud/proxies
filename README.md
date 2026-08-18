# SyndProxy private pool

## Current pool

- Alive now: 646
- Gold now: 219
- HTTP: 194 alive / 35 gold
- HTTPS: 95 alive / 10 gold
- SOCKS4: 170 alive / 101 gold
- SOCKS5: 187 alive / 73 gold

## Historical pool

- Discovered: 86649
- Ever alive: 5726
- Ever gold: 292

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
