# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 416
- HTTP: 123 alive / 63 gold
- HTTPS: 145 alive / 20 gold
- SOCKS4: 178 alive / 165 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41273
- Ever gold: 1320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
