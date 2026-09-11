# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 370
- HTTP: 97 alive / 69 gold
- HTTPS: 47 alive / 23 gold
- SOCKS4: 135 alive / 109 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48721
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
