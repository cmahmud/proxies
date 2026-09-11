# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 420
- HTTP: 93 alive / 68 gold
- HTTPS: 48 alive / 24 gold
- SOCKS4: 177 alive / 165 gold
- SOCKS5: 176 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49018
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
