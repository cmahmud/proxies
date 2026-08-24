# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 389
- HTTP: 137 alive / 54 gold
- HTTPS: 65 alive / 15 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 194 alive / 162 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33606
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
