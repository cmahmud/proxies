# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 389
- HTTP: 93 alive / 68 gold
- HTTPS: 37 alive / 16 gold
- SOCKS4: 175 alive / 152 gold
- SOCKS5: 175 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48168
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
