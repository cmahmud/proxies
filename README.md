# SyndProxy private pool

## Current pool

- Alive now: 745
- Gold now: 392
- HTTP: 197 alive / 76 gold
- HTTPS: 153 alive / 20 gold
- SOCKS4: 190 alive / 147 gold
- SOCKS5: 205 alive / 149 gold

## Historical pool

- Discovered: 148345
- Ever alive: 26427
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
