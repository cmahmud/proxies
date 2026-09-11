# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 436
- HTTP: 104 alive / 76 gold
- HTTPS: 48 alive / 27 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 184 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49161
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
