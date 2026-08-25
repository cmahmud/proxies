# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 413
- HTTP: 91 alive / 65 gold
- HTTPS: 41 alive / 18 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36738
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
