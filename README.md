# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 389
- HTTP: 150 alive / 54 gold
- HTTPS: 41 alive / 15 gold
- SOCKS4: 177 alive / 158 gold
- SOCKS5: 197 alive / 162 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33605
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
