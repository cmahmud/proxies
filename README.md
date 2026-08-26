# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 400
- HTTP: 121 alive / 74 gold
- HTTPS: 149 alive / 21 gold
- SOCKS4: 164 alive / 149 gold
- SOCKS5: 184 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40164
- Ever gold: 1307

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
