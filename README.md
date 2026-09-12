# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 433
- HTTP: 106 alive / 83 gold
- HTTPS: 46 alive / 29 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 179 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49445
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
