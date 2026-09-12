# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 464
- HTTP: 127 alive / 94 gold
- HTTPS: 58 alive / 32 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 193 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49343
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
