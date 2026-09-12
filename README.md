# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 436
- HTTP: 105 alive / 84 gold
- HTTPS: 50 alive / 30 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49444
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
