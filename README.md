# SyndProxy validated proxy pool

## Current pool

- Alive now: 461
- Gold now: 361
- HTTP: 97 alive / 68 gold
- HTTPS: 51 alive / 22 gold
- SOCKS4: 127 alive / 103 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48715
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
