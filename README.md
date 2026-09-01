# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 464
- HTTP: 144 alive / 92 gold
- HTTPS: 122 alive / 38 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 194 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46914
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
