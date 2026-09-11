# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 441
- HTTP: 103 alive / 81 gold
- HTTPS: 54 alive / 27 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49175
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
