# SyndProxy private pool

## Current pool

- Alive now: 828
- Gold now: 386
- HTTP: 234 alive / 75 gold
- HTTPS: 171 alive / 15 gold
- SOCKS4: 214 alive / 147 gold
- SOCKS5: 209 alive / 149 gold

## Historical pool

- Discovered: 148345
- Ever alive: 26467
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
