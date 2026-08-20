# SyndProxy private pool

## Current pool

- Alive now: 765
- Gold now: 388
- HTTP: 189 alive / 82 gold
- HTTPS: 161 alive / 20 gold
- SOCKS4: 220 alive / 144 gold
- SOCKS5: 195 alive / 142 gold

## Historical pool

- Discovered: 149512
- Ever alive: 26919
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
