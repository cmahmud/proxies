# SyndProxy private pool

## Current pool

- Alive now: 839
- Gold now: 350
- HTTP: 249 alive / 77 gold
- HTTPS: 173 alive / 23 gold
- SOCKS4: 187 alive / 118 gold
- SOCKS5: 230 alive / 132 gold

## Historical pool

- Discovered: 167924
- Ever alive: 32595
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
