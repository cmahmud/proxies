# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 451
- HTTP: 112 alive / 79 gold
- HTTPS: 114 alive / 30 gold
- SOCKS4: 173 alive / 164 gold
- SOCKS5: 191 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47373
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
