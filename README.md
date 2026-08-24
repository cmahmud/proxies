# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 379
- HTTP: 103 alive / 48 gold
- HTTPS: 51 alive / 9 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33540
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
