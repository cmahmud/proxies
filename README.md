# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 460
- HTTP: 127 alive / 87 gold
- HTTPS: 132 alive / 34 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 186 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46705
- Ever gold: 1446

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
