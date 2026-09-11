# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 410
- HTTP: 85 alive / 63 gold
- HTTPS: 39 alive / 19 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 179 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48860
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
