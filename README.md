# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 393
- HTTP: 215 alive / 77 gold
- HTTPS: 176 alive / 19 gold
- SOCKS4: 193 alive / 147 gold
- SOCKS5: 210 alive / 150 gold

## Historical pool

- Discovered: 148345
- Ever alive: 26432
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
