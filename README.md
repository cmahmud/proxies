# SyndProxy private pool

## Current pool

- Alive now: 740
- Gold now: 378
- HTTP: 172 alive / 67 gold
- HTTPS: 141 alive / 18 gold
- SOCKS4: 195 alive / 142 gold
- SOCKS5: 232 alive / 151 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25558
- Ever gold: 1064

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
