# SyndProxy validated proxy pool

## Current pool

- Alive now: 656
- Gold now: 389
- HTTP: 163 alive / 65 gold
- HTTPS: 126 alive / 21 gold
- SOCKS4: 172 alive / 150 gold
- SOCKS5: 195 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39556
- Ever gold: 1299

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
