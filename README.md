# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 404
- HTTP: 105 alive / 77 gold
- HTTPS: 42 alive / 17 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 169 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48189
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
