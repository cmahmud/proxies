# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 406
- HTTP: 92 alive / 66 gold
- HTTPS: 35 alive / 21 gold
- SOCKS4: 164 alive / 148 gold
- SOCKS5: 184 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48811
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
