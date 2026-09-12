# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 458
- HTTP: 124 alive / 90 gold
- HTTPS: 63 alive / 33 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 198 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49386
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
