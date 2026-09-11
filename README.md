# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 435
- HTTP: 102 alive / 75 gold
- HTTPS: 51 alive / 28 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49148
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
