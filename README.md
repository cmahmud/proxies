# SyndProxy validated proxy pool

## Current pool

- Alive now: 409
- Gold now: 351
- HTTP: 106 alive / 79 gold
- HTTPS: 45 alive / 24 gold
- SOCKS4: 80 alive / 77 gold
- SOCKS5: 178 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48678
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
