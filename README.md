# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 469
- HTTP: 138 alive / 99 gold
- HTTPS: 68 alive / 37 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49371
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
