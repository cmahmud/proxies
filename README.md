# SyndProxy private pool

## Current pool

- Alive now: 769
- Gold now: 390
- HTTP: 182 alive / 77 gold
- HTTPS: 160 alive / 17 gold
- SOCKS4: 209 alive / 147 gold
- SOCKS5: 218 alive / 149 gold

## Historical pool

- Discovered: 148345
- Ever alive: 26447
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
