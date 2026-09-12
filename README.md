# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 466
- HTTP: 127 alive / 94 gold
- HTTPS: 70 alive / 37 gold
- SOCKS4: 185 alive / 163 gold
- SOCKS5: 195 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49392
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
