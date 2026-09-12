# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 419
- HTTP: 94 alive / 75 gold
- HTTPS: 46 alive / 24 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 170 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49454
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
