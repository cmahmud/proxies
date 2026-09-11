# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 437
- HTTP: 112 alive / 79 gold
- HTTPS: 56 alive / 26 gold
- SOCKS4: 194 alive / 168 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49104
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
