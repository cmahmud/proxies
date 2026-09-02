# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 444
- HTTP: 93 alive / 73 gold
- HTTPS: 104 alive / 32 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 192 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47443
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
