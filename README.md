# SyndProxy validated proxy pool

## Current pool

- Alive now: 672
- Gold now: 403
- HTTP: 136 alive / 80 gold
- HTTPS: 192 alive / 24 gold
- SOCKS4: 168 alive / 146 gold
- SOCKS5: 176 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39959
- Ever gold: 1305

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
