# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 461
- HTTP: 123 alive / 88 gold
- HTTPS: 62 alive / 35 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49387
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
