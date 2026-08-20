# SyndProxy private pool

## Current pool

- Alive now: 1738
- Gold now: 611
- HTTP: 768 alive / 204 gold
- HTTPS: 557 alive / 142 gold
- SOCKS4: 183 alive / 101 gold
- SOCKS5: 230 alive / 164 gold

## Historical pool

- Discovered: 143428
- Ever alive: 24699
- Ever gold: 1032

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
