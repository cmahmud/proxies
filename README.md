# SyndProxy validated proxy pool

## Current pool

- Alive now: 1337
- Gold now: 4
- HTTP: 529 alive / 4 gold
- HTTPS: 135 alive / 0 gold
- SOCKS4: 340 alive / 0 gold
- SOCKS5: 333 alive / 0 gold

## Historical pool

- Discovered: 169115
- Ever alive: 32643
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
