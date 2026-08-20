# SyndProxy private pool

## Current pool

- Alive now: 726
- Gold now: 350
- HTTP: 172 alive / 73 gold
- HTTPS: 184 alive / 19 gold
- SOCKS4: 172 alive / 120 gold
- SOCKS5: 198 alive / 138 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26136
- Ever gold: 1079

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
