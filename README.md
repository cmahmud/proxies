# SyndProxy private pool

## Current pool

- Alive now: 1024
- Gold now: 372
- HTTP: 326 alive / 81 gold
- HTTPS: 275 alive / 23 gold
- SOCKS4: 182 alive / 118 gold
- SOCKS5: 241 alive / 150 gold

## Historical pool

- Discovered: 158225
- Ever alive: 29867
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
