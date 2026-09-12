# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 472
- HTTP: 123 alive / 95 gold
- HTTPS: 66 alive / 38 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 194 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49392
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
