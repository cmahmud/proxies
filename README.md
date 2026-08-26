# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 386
- HTTP: 115 alive / 63 gold
- HTTPS: 97 alive / 20 gold
- SOCKS4: 171 alive / 148 gold
- SOCKS5: 187 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39338
- Ever gold: 1298

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
