# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 427
- HTTP: 127 alive / 77 gold
- HTTPS: 140 alive / 23 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 200 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42400
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
