# SyndProxy private pool

## Current pool

- Alive now: 909
- Gold now: 392
- HTTP: 301 alive / 93 gold
- HTTPS: 181 alive / 14 gold
- SOCKS4: 229 alive / 157 gold
- SOCKS5: 198 alive / 128 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18236
- Ever gold: 717

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
