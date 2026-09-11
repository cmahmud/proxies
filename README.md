# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 440
- HTTP: 107 alive / 78 gold
- HTTPS: 49 alive / 28 gold
- SOCKS4: 186 alive / 165 gold
- SOCKS5: 176 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49118
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
