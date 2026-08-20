# SyndProxy private pool

## Current pool

- Alive now: 755
- Gold now: 386
- HTTP: 178 alive / 76 gold
- HTTPS: 146 alive / 15 gold
- SOCKS4: 214 alive / 146 gold
- SOCKS5: 217 alive / 149 gold

## Historical pool

- Discovered: 148345
- Ever alive: 26451
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
